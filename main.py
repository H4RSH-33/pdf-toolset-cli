from PyPDF2 import PdfWriter,PdfReader

def show_welcome():
    print("\n" + "="*50)
    print("🛠️  WELCOME TO PDF TOOLSET (Made with Python)  🛠️")
    print("="*50)
    
def options():
            print("\n" + "="*50)
            print("Choose one of the following options:\n")
            print("1️⃣  Merge multiple PDFs")
            print("2️⃣  View PDF information")
            print("3️⃣  Compress a PDF")
            print("4️⃣  Add blank pages at start/end")

def PDF_merger():
    merger = PdfWriter()
    Pdfs = []

    n = int(input("Enter the number of PDF's you want merger:"))

    for i in range(0,n):
        Name_of_PDF = input(f"Enter the name of the PDF {i+1}(With extension .pdf):")
        merger.append(Name_of_PDF)

    for Pdf in Pdfs:
        merger.append(Pdf)

    merger.write("Merged_PDF.pdf")
    print("Merging done👍\nMerged PDF is created with name Merged_PDF\nYou access your merged PDF from there!")
    merger.close()


def PDF_metadata():
    name = input("Enter the PDF file name (without .pdf): ")
    reader = PdfReader(name+".pdf")

    meta = reader.metadata

    print("There is/are",len(reader.pages),"pages in your PDF")

    # All of the following could be None!
    print("Author:",meta.author)
    print("Creator:",meta.creator)
    print("Producer:",meta.producer)
    print("PDF subject:",meta.subject)
    print("PDF title:",meta.title)

def PDF_compressor():
    name_of_PDF=input("Enter just the name of PDF:")
    reader = PdfReader(name_of_PDF+".pdf")
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()  
        writer.add_page(page)

    with open(name_of_PDF+"_Compressed.pdf", "wb") as f:
        writer.write(f)

def add_blank_pages_start_or_end():
    name = input("Enter the PDF file name (without .pdf): ")

    try:
        reader = PdfReader(name + ".pdf")
    except FileNotFoundError:
        print("❌ File not found. Make sure the file is in the current directory.")
        return

    if len(reader.pages) == 0:
        print("❌ The PDF has no pages.")
        return

    writer = PdfWriter()
    first_page = reader.pages[0]
    width = first_page.mediabox.width
    height = first_page.mediabox.height

    where = input("Where do you want to add blank pages? Type 'start' or 'end': ").strip().lower()
    try:
        num_pages = int(input("How many blank pages do you want to add? "))
    except ValueError:
        print("❌ Invalid number.")
        return

    if where not in ['start', 'end']:
        print("❌ Invalid input. Please type 'start' or 'end'.")
        return

    if where == "start":
        
        for _ in range(num_pages):
            writer.add_blank_page(width=width, height=height)

    for page in reader.pages:
        writer.add_page(page)

    if where == "end":
        
        for _ in range(num_pages):
            writer.add_blank_page(width=width, height=height)

    output_name = name + f"_with_blank_pages_at_{where}.pdf"
    with open(output_name, "wb") as f:
        writer.write(f)

    print(f"✅ PDF saved as '{output_name}' with {num_pages} blank page(s) at the {where}.")

use_again = "y"
show_welcome()
while(use_again != "n"):    
    options()
    try:
        user_inp = int(input("Enter your input here:"))
        match user_inp:
            case 1:
                PDF_merger()
            case 2:
                PDF_metadata()
            case 3:
                PDF_compressor()
            case 4:
                add_blank_pages_start_or_end()
            case _:
                print("Invalid input")
                raise ValueError
    except ValueError:
        print("Please enter the valid input between 1 to 4")
    except FileNotFoundError:
        print("❌ File not found. Please check the filename and try again.")
    except Exception as e:
        print("Some error occured",e)
    finally:       
                use_again = input("🔁 Do you want to use the toolset again? (Y/N): ").strip().lower()
                if use_again not in ['y', 'yes']:
                    print("👋 Bye! Thanks for using the toolset.")
                    print("====================")
                    break

            