from fpdf import FPDF


class PDF(FPDF):
    def top(self):
        self.set_font("helvetica", "B", 48)
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        self.cell(
            width,
            50,
            self.title,
            align="C",
            )

    def shirt(self, name):
        self.image("shirtificate.png", x=15, y=75, w=180)
        self.set_font("helvetica", "B", 24)
        self.set_text_color(255, 255, 255)
        width = self.get_string_width(f"{name} took CS50") + 6
        self.set_x((210 - width) / 2)
        self.cell(
            width,
            250,
            f"{name} took CS50",
            align="C"
            )

    def print_shirtificate(self, name):
        self.add_page()
        self.top()
        self.shirt(name)

    @staticmethod
    def get_name():
        return input("Name: ").strip().capitalize()


def main():
    name = PDF.get_name()
    # Make magic happen
    pdf = PDF()
    pdf.set_title("CS50 Shirtificate")
    pdf.print_shirtificate(name)
    pdf.output("shirtificate.pdf")


if __name__ in "__main__":
    main()

