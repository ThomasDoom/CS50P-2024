from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Hello World!", 1)
pdf.ln()
pdf.cell(60, 10, "Lol its 3am", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.output("tuto1.pdf")
