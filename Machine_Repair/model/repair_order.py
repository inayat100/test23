from odoo import models , fields,api
from datetime import date
class RepairOrder(models.Model):
    _name = "repairorder"
    

    @api.onchange('client')
    def _onchange_(self):
        print(self.client.country_id.name)
        self.street = self.client.street
        self.street2 = self.client.street2
        self.city = self.client.city
        self.state = self.client.name
        self.zip = self.client.zip
        self.country = self.client.country_id.name
        self.email = self.client.email
        self.phone = self.client.phone
    
    def write(self,vals):
       vals['date_of_receipt'] = date.today()
       res = super(RepairOrder,self).write(vals)
       return res

    @api.model
    def create(self,vals): 
       vals['sqn'] = self.env['ir.sequence'].next_by_code('repairorder')
       print(vals['sqn'],"===========================")
       vals['form_bool'] = True
       res = super(RepairOrder,self).create(vals)
       return res


    sqn = fields.Char("sequence number",index=True,readonly=True,copy=False,default='new')
    subject = fields.Char("Subject")
    assigned_to = fields.Many2one("res.users","Assigned to")
    priority = fields.Selection([("0","0"),("1","1"),("2","2")],"Priority")
    date_of_receipt = fields.Date("Date Of Receipt",default=date.today())
    client = fields.Many2one("res.partner","Client")
    contact_name = fields.Char("Contact Name")
    # phone = fields.Char("Phone",related='client.phone', store=True)
    phone = fields.Char("Phone")
    mobile = fields.Char("Mobile")
    email = fields.Char("E-mail")
    contact_number = fields.Char("Contact Number")
    street = fields.Char(" ")
    street2 = fields.Char(" ")
    city = fields.Char(" ")
    state = fields.Char(" ")
    zip = fields.Char(" ")
    country = fields.Char(" ")
    reapair_order_lines = fields.One2many("repairorder.line","repair_order_id","Repair Order Lines")
    form_bool = fields.Boolean("Bool ")

class RepairOrderLines(models.Model):
    _name = "repairorder.line"

    repair_order_id = fields.Many2one("repairorder","Repair Order Id")
    machine = fields.Many2one("product.template","Machine")
    machine_name = fields.Char("Machine Name")
    machine_model = fields.Char("Model #")
    serial_number = fields.Integer("Serial Number")

    under_guarantee = fields.Selection([("yes","YES"),("no","NO")],"Under Guarantee")
    guarantee_type = fields.Selection([("paid","Paid"),("free","Free")],"Guarantee Type")
    nature_of_service = fields.Char("Nature of Service")




