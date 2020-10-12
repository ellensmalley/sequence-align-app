from Bio import SeqIO, Entrez
from Bio.Seq import Seq
import random
import os.path
from django.contrib.staticfiles.storage import staticfiles_storage
import re

class AlignmentService:
	genome_list = ['NC_000852', 'NC_007346', 'NC_008724', 'NC_009899', 'NC_014637', 'NC_020104', 'NC_023423', 'NC_023640', 'NC_023719', 'NC_027867']

	# Not using method due to risk of surpassing limits on Entrez access
	# def fetch_sequence_file_and_save(self, sequence_name, filename):
		# Entrez.email = "e.smalley117@gmail.com"
		# handle = Entrez.efetch(db="nucleotide", id=sequence_name, rettype="gb", retmode="text")
		# f = open(filename, "w+")
		# f.write(handle.read())
		# f.close()

	def is_valid_sequence(self, sequence, search=re.compile(r'[^ATGCatgc]').search):
		return not (bool(search(sequence)))

	def find_location_details(self, sequence_record, int_location):
		for feature in sequence_record.features:
			if int_location in feature and feature.type == "CDS":
				return { "genome": sequence_record.name, "protein": feature.qualifiers.get("protein_id")[0], "location": str(int_location)}
		return { "genome": sequence_record.name, "protein": "", "location": str(int_location)}

	def find_alignment(self, sequence):
		sequence = sequence.upper()
		if not self.is_valid_sequence(sequence):
			return {"genome": "INVALID", "protein": "INVALID", "location": "INVALID"}
		sequence_rc = str(Seq(sequence).reverse_complement())
		random.shuffle(self.genome_list)
		possible_locations = []
		for genome in self.genome_list:
			filename = staticfiles_storage.path("sequenceFiles/" + genome + ".gb.txt")
			if not os.path.isfile(filename):
				raise Exception('Cannot find specified file ', filename)
			record = SeqIO.read(filename, "genbank")
			location = record.seq.find(sequence)
			location_rc = record.seq.find(sequence_rc)
			for loc in [location, location_rc]:
				if (loc != -1):
					possible_location = self.find_location_details(record, loc)
					if (possible_location.get("protein") == ""):
						possible_locations.append(possible_location)
					else:
						return possible_location
		# hasn't returned protein value yet, check if sequence is at least present in some genome
		if len(possible_locations) > 0:
			return possible_locations[0]
		return {"genome": "", "protein": "", "location": ""}

	
