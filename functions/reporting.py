from fpdf import FPDF


class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Campaign Performance Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')


def generate_pdf_report(actions, filename="report.pdf"):
    """
    Generate a PDF report for campaign recommendations.

    Args:
        actions (list): List of campaign action dictionaries.
        filename (str): File path to save the PDF report.
    """
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    for action in actions:
        pdf.cell(0, 10, f"Campaign ID: {action['campaign_id']}", 0, 1)
        pdf.cell(0, 10, f"Current Status: {action['current_status']}", 0, 1)
        pdf.cell(0, 10, f"Status Reason: {action['current_status_reason']}", 0, 1)
        pdf.cell(0, 10, f"Recommended Action: {action['action']}", 0, 1)
        pdf.cell(0, 10, f"Reason: {action['reason']}", 0, 1)
        pdf.cell(0, 10, '', 0, 1)  # Empty line for spacing

    pdf.output(filename)
