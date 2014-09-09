# -*- coding:utf-8 -*-
#KEGG的某物种gene-->protein sequence list（fasta）
#guoyang
import urllib
import sys

def get_gene_list(name):
	link='http://rest.kegg.jp/list/'+name
	gene_list=[]
	try:
		content=urllib.urlopen(link)
		lines=content.readlines()
		for eachLine in lines:
			gene_list.append(eachLine.split('\t')[0].strip()+'\n')
	except:
		print 'gene LIST try again...'
		gene_list=get_gene_list(name)
	return gene_list

def get_gene_protein(gene):
	link='http://rest.kegg.jp/get/'+gene+'/aaseq'
	try:
		content=urllib.urlopen(link)
		lines=content.readlines()
	except:
		print gene+' try again...'
		lines=get_gene_protein(gene)
	return lines
	
if __name__ == '__main__':
	name=sys.argv[1]
	gene_list=get_gene_list(name)
	open(name+'_gene_list.txt','w').writelines(gene_list)
	gene_protein=[]
	for each in gene_list:
		print each
		gene_protein+=get_gene_protein(each.strip())
	open(name+'_protein_sequences.fasta','w').writelines(gene_protein)
