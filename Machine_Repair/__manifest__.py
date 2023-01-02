
{
    'name': 'Machine Repair',
    'version': '1.0',
    'website':"https://www.diracerp.com",
    'image':[],
    'depends': ['contacts','base',
                
                ],
    'author':"inayat",
    'description': "this is Machine Repair models",
    'data': ["security/ir.model.access.csv",
             "data/seq_product.xml",
             "data/sequence.xml",
             "view/repair_order_view.xml",
             "view/product_view.xml",
           
            ],
    'installable': True,
    'auto_install': False,
    'active':False,
}