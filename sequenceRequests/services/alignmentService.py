from Bio import SeqIO, Entrez
from Bio.Seq import Seq
import random

class AlignmentService:

	def findAlignment(sequence_string):
		protein_list = ['NC_000852', 'NC_007346', 'NC_008724', 'NC_009899', 'NC_014637', 'NC_020104', 'NC_023423', 'NC_023640', 'NC_023719', 'NC_027867']
		random.shuffle(protein_list)
		for protein in protein_list:
			if encodes_protein(sequence_string, protein):
				return protein
		return None
			
	def pad_sequence(sequence):
	    remainder = len(sequence) % 3
	    if remainder == 0 :
	        return sequence
	    else :
	        return sequence + Seq('N' * (3 - remainder))

	def encodes_protein(sequence_string, protein_id):
		# ideally would not be hard coded and would be a distribution list 
		# email used for notifications if entrez request limits are abused
		Entrez.email = "e.smalley117@gmail.com"
		handle = Entrez.efetch(db="nuccore", id=protein_id, rettype="fasta", retmode="text")

		sequence_record = SeqIO.read(handle, "fasta")
		sequence_object = sequence_record.seq
		sequence_object = pad_sequence(sequence_object)

		protein_transcription = sequence_object.transcribe()
		protein_translation = str(protein_transcription.translate())

		protein_transcription2 = pad_sequence(Seq("N") + sequence_object).transcribe()
		protein_translation2 = str(protein_transcription2.translate())

		protein_transcription3 = pad_sequence(Seq("NN") + sequence_object).transcribe()
		protein_translation3 = str(protein_transcription3.translate())

		compareSequence = Seq(sequence_string)
		compareSequence = pad_sequence(compareSequence)

		compareTranscription = compareSequence.transcribe()
		compareTranslation = compareTranscription.translate()

		compareTranscription2 = pad_sequence(Seq("N") + compareSequence).transcribe()
		compareTranslation2 = compareTranscription2.translate()

		compareTranscription3 = pad_sequence(Seq("NN") + compareSequence).transcribe()
		compareTranslation3 = compareTranscription3.translate()


		return (str(compareTranslation) in str(protein_translation)
		      or str(compareTranslation) in str(protein_translation2)
		      or str(compareTranslation) in str(protein_translation3)
		      or str(compareTranslation2) in str(protein_translation)
		      or str(compareTranslation2) in str(protein_translation2)
		      or str(compareTranslation2) in str(protein_translation3)
		      or str(compareTranslation3) in str(protein_translation)
		      or str(compareTranslation3) in str(protein_translation2)
		      or str(compareTranslation3) in str(protein_translation3))
			