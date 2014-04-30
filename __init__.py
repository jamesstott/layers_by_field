# -*- coding: utf-8 -*-

def classFactory(iface):
  from layers_by_field import layers_by_field
  return layers_by_field(iface)
