from src.assignments.assignment9.invoice import Invoice
from src.assignments.assignment9.invoice_item import InvoiceItem

#Write import statements for classes invoice and invoice_item
'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object
In the loop:
Create a new InvoiceItem
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''

invoice= Invoice('ABC','03/29/2018')
again='y'

while again == 'y':
        
        
    description = input("Enter a description of the items: ")
    quantity = int(input("Enter the quantity of items: "))
    cost = float(input("Enter the cost per item: "))
        
    invoice_item = InvoiceItem(description, quantity, cost)
    invoice.add_invoice_item(invoice_item)
        
    again = input("Would you like to continue? y/n...")

    if again != 'y':
        invoice.print_invoice()
 
