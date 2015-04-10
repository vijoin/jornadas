# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
from openerp.osv import fields,osv

class trabajadores(osv.osv):
    """Registro de Trabajadores"""
    _name = 'trabajadores'
    _rec_name = 'cedula'
    _columns = {
        'cedula': fields.char(string="Cédula", size=8, required=True, index=True, help="Cédula del Trabajador"),
        'nombre_completo': fields.char(string="Nombre Completo", size=80, required=True, help="Nombre Completo del Trabajador"),
        'dependencia': fields.char(string="Dependencia", size=100, required=True, help="Dependencia del Trabajador"),
    }
trabajadores()

class beneficiados(osv.osv):
    """Registro de Beneficiados Inces"""
    _name = 'beneficiados'
    _columns = {
        'trabajadores_id': fields.many2one('trabajadores', 'Cédula del Trabajador', help='Cédula del trabajador beneficiado'),
        'jornadas_id': fields.many2one('jornadas', 'Jornada Activa', help='Jornada previamente definida en la configuración'),
        'articulos_ids' : fields.many2many('articulos', 'articulos_beneficiados_rel', 'beneficiados_id', 'articulos_id','Articulos a Comprar'),
	'fec_compra': fields.datetime('Fecha de Compra'),
    }
beneficiados()

class jornadas(osv.osv):
    """Definición de Jornadas"""
    _name = 'jornadas'
    _rec_name = 'titulo'
    _columns = {
        'codigo': fields.char('Código', size=5, required=True, help="Código único (max 5 dígitos)"),
        'titulo': fields.char('Título', size=100, required=True, index=True, help="Título de la Jornada"),
        'descripcion': fields.text('Descripción', help="Descripción ampliada de la Jornada"),
        'lugar': fields.char('Lugar', size=100, help="Lugar donde se realiza la jornada"),
        'fecha_inicio': fields.date('Fecha de Inicio', help="Fecha de inicio de la jornada"),
        'fecha_culminacion': fields.date('Fecha de Culminación', help="Fecha de Culminación de la Jornada"),
        'institucion': fields.char('Institución', size=50, help="Insitución que ofrece la Jornada"),
        'articulos_ids': fields.one2many('articulos', 'jornadas_id', 'Artículos ofrecidos en la jornada', help='Predefinición de artículos que se ofrecerán en la jornada'),
        'responsable': fields.char('Responsable de la Jornada', size= 40, help='Nombre completo del responsable de la jornada'),
        'tel_responsable': fields.char('Teléfono del responsable', size=11, help='Teléfono del responsable de la jornada'),
        'active': fields.boolean('Activa'),
    }
jornadas()

class articulos(osv.osv):
    """Artículos"""
    _name = 'articulos'
    _rec_name = 'nombre'
    _columns = {
        'codigo': fields.char("Código:", size=5, required=True, help="Código del Artículo (max 5 caracteres)"),
        'nombre': fields.char('Nombre', size=80, required=True, index=True, help="Nombre corto para el artículo"),
        'descripcion': fields.text('Descripcion', help="Descripción completa del artículo"),
        'categoria': fields.selection([('telecomunicaciones',"Telecomunicaciones"),('alimentos',"Alimentos"),('electrodomesticos',"Electrodomésticos"),('medico-asistencial',"Médico-Asistencial")], 'Categoría'),
        'jornadas_id': fields.many2one('jornadas', "Jornadas"),
        'beneficiados_id': fields.many2one('beneficiados', "Beneficiados"),
    }
articulos()
