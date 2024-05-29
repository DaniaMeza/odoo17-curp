# -*- coding: utf-8 -*-
from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    curp = fields.Char(string='CURP Personalizado')  # Cambia 'CURP Personalizado' por la etiqueta que desees

    @api.constrains('curp')
    def _check_curp(self):
        """Validar el formato del CURP y su longitud."""
        pattern = re.compile(r'^[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z0-9]{2}$')
        for record in self:
            if record.curp:
                # Verificar la longitud del CURP
                if len(record.curp) != 18:
                    raise ValidationError('El CURP debe tener exactamente 18 caracteres.')
                # Verificar el formato del CURP
                elif not pattern.match(record.curp):
                    raise ValidationError('El CURP debe tener el formato correcto.')
