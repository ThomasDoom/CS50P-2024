from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 48)
        self.cell(0, 50, "CS50 Shirtificate", align="C")

    def shirtificate(self, name):
        self.add_page()
        self.image("shirtificate.png", x=15, y=75, w=180)
        self.set_font("helvetica", "B", 24)
        self.set_text_color(255, 255, 255)
        self.set_y(140)
        self.cell(0, 10, f"{name} took CS50", align="C")


def main():
    name = input("Name: ").strip()
    pdf = PDF()
    pdf.shirtificate(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
