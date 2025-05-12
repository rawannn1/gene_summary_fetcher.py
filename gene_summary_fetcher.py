from Bio import Entrez

Entrez.email = "your@email.com"  # <- Change this to your email

gene_name = input("Enter a gene symbol (e.g., DRD4): ")

handle = Entrez.esearch(db="gene", term=f"{gene_name}[sym] AND Homo sapiens[orgn]")
record = Entrez.read(handle)
handle.close()

if record["IdList"]:
    gene_id = record["IdList"][0]
    handle = Entrez.efetch(db="gene", id=gene_id, retmode="xml")
    records = Entrez.read(handle)
    handle.close()
    summary = records[0]["Entrezgene_summary"]
    print(f"Summary for {gene_name}:\n{summary}")
else:
    print("Gene not found in NCBI.")
