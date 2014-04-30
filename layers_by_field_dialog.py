############################################
#
# Split layers by field.
# Developed by James Stott
# 26/06/2013
# Based on the code of the Split Shapefile plugin.
#
###############################################

# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from layersbyfielddialogbase import Ui_LayersByFieldDialog
from qgiscombomanager import *

class layers_by_field_dialog( QDialog, Ui_LayersByFieldDialog ):
  
  
  def __init__( self, iface ):
    QDialog.__init__( self )
    self.setupUi( self )
    self.iface = iface
    
    self.layerComboManager = VectorLayerCombo(self.inputLayerCombo,"",{"hasGeometry": True})
    self.fieldComboManager = FieldCombo(self.splitFieldCombo, self.layerComboManager)
    
    self.btnOk = self.buttonBox.button( QDialogButtonBox.Ok )

  def reject( self ):
    QDialog.reject( self )

  def accept( self ):
    
    if self.inputLayerCombo.currentText() == "":
      QMessageBox.information( self, QCoreApplication.translate( 'layers_by_field_dialog', "Layers From Field" ), QCoreApplication.translate( 'layers_by_field_dialog', "No input layer specified" ) )
    else:

      inField = self.fieldComboManager.getFieldName()
      inFieldIdx = self.fieldComboManager.getFieldIndex()
      inLayer = self.layerComboManager.getLayer()

      self.btnOk.setEnabled( True )

      self.split( inLayer, inField, inFieldIdx )

      self.reject()
    
  def split( self, layer, field, index ):
    
    vProvider = layer.dataProvider()
    
    uniques = vProvider.uniqueValues(index)

    allAttrs = vProvider.attributeIndexes()
    
    self.progressBar.setRange( 0, len( uniques ) )
    self.progressBar.setValue( 0 )

    j = 0

    for i in uniques[0:]:
        
        if unicode(vProvider.name()) == "postgres":
        
            self.vlayer = QgsVectorLayer(vProvider.dataSourceUri(), unicode(layer.name()) + "_" + unicode(uniques[j]), "postgres")
        
        elif unicode(vProvider.name()) == "ogr":
        
            self.vlayer = QgsVectorLayer(vProvider.dataSourceUri(), unicode(layer.name()) + "_" + unicode(uniques[j]), "ogr")

        sqlstring = field + " = '" + unicode(uniques[j]) + "'"
        j = j+1
        self.vlayer.setSubsetString( sqlstring )
        QgsMapLayerRegistry.instance().addMapLayer(self.vlayer)
        self.progressBar.setValue( self.progressBar.value() + 1 )
    self.progressBar.setValue( 0 )

