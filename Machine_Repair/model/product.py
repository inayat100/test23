from odoo import models,fields,api

       
class Product(models.Model):
    _name = "product"

    @api.model
    def create(self,vals): 
       vals['sqnp'] = self.env['ir.sequence'].next_by_code('product')
       print(vals['sqnp'],"===========================")
       res = super(Product,self).create(vals)
       return res

    def fn1(self):
        print("################################")
    def fn2(self):
        print("################################")
    image = fields.Binary(" ")
    name = fields.Char(" ")
    sold = fields.Boolean(" ")
    purchased = fields.Boolean(" ")

# -------------------------------
    sqnp = fields.Char("SNO",index=True,readonly=True,copy=False,default="NEW")
    product_type = fields.Char("Product Type")
    internal_reference = fields.Char("Internal Reference")
    barcode = fields.Char("Barcode")
    machine = fields.Boolean("Machine")
    product_category = fields.Char("Product Category")
    sale_price = fields.Char("Sale Price")
    customer_taxes = fields.Char("Customer Taxes") 
    cost = fields.Float("Cost")
    company = fields.Char("Company")
    unit_of_measure = fields.Char("Unit of Measure")
    purchased_unit_of_measure = fields.Char("purchased Unit of Measure")