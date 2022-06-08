# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class Wine(models.Model):
    _inherit = 'product.template'
    _order = 'winetype_id desc'

    country_id = fields.Many2one('ov_wine.country',
                                 string="Country", index=True)
    region_id = fields.Many2one('ov_wine.region',
                                string="Region", index=True)
    city_id = fields.Many2one('ov_wine.city',
                              ondelete='set null', string="City", index=True)
    producer_id = fields.Many2one('ov_wine.producer',
                                  ondelete='set null', string="Producer", index=True)
    swk_city_id = fields.Many2one('ov_wine.swk_city',
                                  string="SWK", index=True)
    winetype_id = fields.Many2one('ov_wine.winetype',
                                  string="Winetype", index=True)
    vintage_year_id = fields.Many2one('ov_wine.vintage_year',
                                      string="Vintage Year", index=True)
    grapes = fields.Many2many('ov_wine.grape', string='Grapes')
    storable_year_id = fields.Many2one('ov_wine.storable_year',
                                       ondelete='set null', string="Storable Year", index=True)
    alcohol = fields.Float('Alcohol', digits=(3, 1))
    serving_temp_id = fields.Many2one('ov_wine.serving_temp',
                                      ondelete='set null', string="Serving temp", index=True)
    wine_aging = fields.Text(string="Aging", help="Making of wine")
    description = fields.Html(string="Description")
    our_comment = fields.Html(string="Our comment")
    food_pairing = fields.Many2many('ov_wine.food', string='Food')
    pricelist_ids = fields.One2many('product.pricelist.item', 'product_tmpl_id', 'Prices')
    product_nr = fields.Text(string="Product Nr.")
    
    sustainabilitytype_id = fields.Many2one('ov_wine.sustainabilitytype',
                                        ondelete='set null', string="Sustainability type", index=True)
    best_drinking_age = fields.Text(string="Best drinking age")
    wine_award = fields.Text(string="Wine award")
    wine_tags = fields.Many2many('ov_wine.wine_tags', string='wine tags')


class BottleSize(models.Model):
    _inherit = 'uom.uom'
    _order = "order"
    order = fields.Integer()


class Producer(models.Model):
    _name = 'ov_wine.producer'
    _description = "wine producer description"
    _order = "order"
    name = fields.Char(string="Producer", required=True, help="Name of the producer to be shown in the shop")
    description = fields.Text()
    order = fields.Integer()
    description_html = fields.Html(string="description_html")
    address_id = fields.Many2one('res.partner',
                                 ondelete='set null', string="address", index=True)


class Winetype(models.Model):
    _name = 'ov_wine.winetype'
    _description = "Wine Type"
    _order = "order"
    name = fields.Char(string="Type", required=True, help="Common Types of Wine (red, white,..)")
    description = fields.Text()
    order = fields.Integer()


class Sustainabilitytype(models.Model):
    _name = 'ov_wine.sustainabilitytype'
    _description = "Sustainability Type"
    _order = "order"
    name = fields.Char(string="Type", required=True, help="Sustainability Types of Wine")
    description = fields.Text()
    order = fields.Integer()


class Country(models.Model):
    _name = 'ov_wine.country'
    _description = "country names"
    _order = "order"
    name = fields.Char(string="Country", required=True, help="Country of origin (Switzerland, France, Italy, ..)")
    description = fields.Text()
    order = fields.Integer()


class VintageYear(models.Model):
    _name = 'ov_wine.vintage_year'
    _description = "vintage year"
    _rec_name = 'year'
    _order = "order"
    year = fields.Char(string="Vintage_Year", size=4, required=True)
    order = fields.Integer()


class StorableYear(models.Model):
    _name = 'ov_wine.storable_year'
    _description = "storable year"
    _rec_name = 'year'
    _order = "order desc"
    year = fields.Char(string="Storable_Year", size=4, required=True)
    order = fields.Integer()


class ServingTemp(models.Model):
    _name = 'ov_wine.serving_temp'
    _description = "serving temp"
    _order = "order"
    name = fields.Char(string="Serving temp.", required=True)
    order = fields.Integer()


class Grape(models.Model):
    _name = 'ov_wine.grape'
    _description = "grape name"
    _order = "order"
    name = fields.Char(string="Grape", required=True, help="Name of the grape - (Barbera, Cabernet Sauvignon,...)")
    description = fields.Text()
    order = fields.Integer()


class Food(models.Model):
    _name = 'ov_wine.food'
    _description = "food name"
    _order = "order"
    name = fields.Char(string="Food", required=True, help="Name of the food")
    description = fields.Text()
    order = fields.Integer()


class wine_tags(models.Model):
    _name = 'ov_wine.wine_tags'
    _description = "wine tags"
    _order = "order"
    name = fields.Char(string="wine_tags", required=True, help="wine tags")
    description = fields.Text()
    order = fields.Integer()


class Region(models.Model):
    _name = 'ov_wine.region'
    _description = "region names"
    _order = "order"
    name = fields.Char(string="Region", required=True, help="Region of Wine (Piemont, Tuscany, Sicily,..)")
    description = fields.Text()
    order = fields.Integer()
    country_id = fields.Many2one('ov_wine.country',
                                 ondelete='set null', string="Country", index=True)


class City(models.Model):
    _name = 'ov_wine.city'
    _description = "city names"
    _order = "order"
    name = fields.Char(string="City", required=True, help="City of Wine-origin")
    description = fields.Text()
    order = fields.Integer()
    region_id = fields.Many2one('ov_wine.region',
                                ondelete='set null', string="Region", index=True)


class SWK_Category(models.Model):
    _name = 'ov_wine.swk_category'
    _description = "swk category"
    _order = "order"
    name = fields.Char(string="SWK Category", required=True, help="SWK Top Level Category")
    description = fields.Text()
    order = fields.Integer()


class SWK_Region(models.Model):
    _name = 'ov_wine.swk_region'
    _description = "swk region"
    _order = "order"
    name = fields.Char(string="SWK Region", required=True, help="SWK Region")
    description = fields.Text()
    order = fields.Integer()
    category_id = fields.Many2one('ov_wine.swk_category',
                                  ondelete='set null', string="Category")


class SWK_City(models.Model):
    _name = 'ov_wine.swk_city'
    _description = "swk city"
    _order = "order"
    name = fields.Char(string="SWK City", required=True, help="SWK City")
    description = fields.Text()
    order = fields.Integer()
    swk_region_id = fields.Many2one('ov_wine.swk_region',
                                    ondelete='set null', string="SWK Region ID")
    swk_code = fields.Integer(required=True)
