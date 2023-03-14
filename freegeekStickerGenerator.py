import PyPDF2
from fpdf import FPDF
from csv import writer
from datetime import datetime

def generate_x_pages(pages):
    #Open nextID file, save nextID as a variable
    f = open("nextID.txt", "r")
    nextID = int(f.read())
    f.close()

    #Create PDF 
    new = "StickersID_" + str(nextID) + "-" + str(nextID + ((80 * pages) - 1)) + ".pdf"


    labels = FPDF('P', 'mm', 'Letter')

    labels.set_margins(8,13)
    labels.set_auto_page_break(True,13)

    labels.add_page()

    labels.set_font("Courier", size = 15)
    
    timestamps = []

    # create a cell
    #labels.cell(-2)
    for i in range(1, (20 * pages) + 1):
        labels.cell(44, 12.6, txt = "ID#:" + str(nextID),
                 ln = 0, align = 'L')
        timestamps.append([str(datetime.now()), str(nextID)])
        labels.cell(8)
        nextID = nextID + 1
        labels.cell(44, 12.6, txt = "ID#:" + str(nextID),
                 ln = 0, align = 'L')
        timestamps.append([str(datetime.now()), str(nextID)])
        labels.cell(8)
        nextID = nextID + 1
        labels.cell(44, 12.6, txt = "ID#:" + str(nextID),
                 ln = 0, align = 'L')
        timestamps.append([str(datetime.now()), str(nextID)])
        labels.cell(8)
        nextID = nextID + 1
        labels.cell(44, 12.6, txt = "ID#:" + str(nextID),
                 ln = 2, align = 'L')
        timestamps.append([str(datetime.now()), str(nextID)])
        nextID = nextID + 1
        labels.cell(-156)


    # save the pdf with name .pdf
    labels.output(new)
    
    #Update CSV file
    with open("GenerationDates.csv", "a") as csvfile: 
        csvwriter = writer(csvfile)
        csvwriter.writerow([])
        csvwriter.writerows(timestamps)
        csvfile.close()



    #Overwrite nextID with new 
    f = open("nextID.txt", "w")
    f.write(str(nextID))
    f.close()
    

if __name__ == '__main__':
    pages = int(input("Enter the number of pages of stickers you would like to print: "))
    generate_x_pages(pages)