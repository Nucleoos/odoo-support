# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
from erppeek import Client


class Contract(models.Model):
    _name = 'support.contract'
    _description = 'support.contract'

    name = fields.Char(
        'Name',
        required=True,
        )
    server_host = fields.Char(
        string='Server Host',
        required=True,
        help="Specified the port if port different from 80. For eg you can use: \
        * ingadho.com\
        * ingadhoc.com:8069"
        )
    number = fields.Char(
        string='Number',
        required=True,
        )

    @api.multi
    def get_connection(self):
        db_list = self.get_client().db.list()
        print 'db_list', db_list
        if db_list:
            return self.get_client(db_list[0])
        else:
            raise Warning(_("Could not fine any database on socket '%s'") % (
                self.server_host))

    @api.multi
    def get_client(self, database=False):
        self.ensure_one()
        Client.db.list()
        if not database:
            return Client(
                'http://%s' % (self.server_host))
        else:
            return Client(
                'http://%s' % (self.server_host),
                db=database,
                user=self.name,
                password=self.number)

    @api.one
    def get_state():
        raise Warning(_('Not implemented yet!'))

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: