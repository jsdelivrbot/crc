#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
from datetime import datetime
from django.conf import settings


class PathFile(object):

    _ddirDB = settings.DIRDB

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, basestring):
                setattr(self, key, value)
            else:
                setattr(self, key, value[0])

    @property
    def nc(self):
        if 'res' in self.resospatiale:
            self.resospatiale = self.resospatiale[3:]
        if self.produit == 'seviri_aerus':
            fichier = 'seviri_r'+self.resospatiale+'_'+self.pasdetemps+'.nc'
        else:
            fichier = self.produit+'_r'+self.resospatiale+'_'+self.pasdetemps+'.nc'
        return os.path.join(self._ddirDB, self.type, self.capteur, self.produit, 'res'+self.resospatiale, fichier)

    @property
    def nc1(self):
        if 'res' in self.resospatiale1:
            self.resospatiale1 = self.resospatiale1[3:]
        if self.produit1 == 'seviri_aerus':
            fichier = 'seviri_r'+self.resospatiale1+'_'+self.pasdetemps1+'.nc'
        else:
            fichier = self.produit1+'_r'+self.resospatiale1+'_'+self.pasdetemps1+'.nc'
        return os.path.join(self._ddirDB, self.type1, self.capteur1, self.produit1, 'res'+self.resospatiale1, fichier)
    
    @property
    def nc2(self):
        if 'res' in self.resospatiale2:
            self.resospatiale2 = self.resospatiale2[3:]
        if self.produit2 == 'seviri_aerus':
            fichier = 'seviri_r'+self.resospatiale2+'_'+self.pasdetemps2+'.nc'
        else:
            fichier = self.produit2+'_r'+self.resospatiale2+'_'+self.pasdetemps2+'.nc'
        return os.path.join(self._ddirDB, self.type2, self.capteur2, self.produit2, 'res'+self.resospatiale2, fichier)
    
    @property
    def csv(self):
        try:
            pathcsv = os.path.join(self._ddirDB, 'in_situ', self.mesure, 'niveau_'+ self.niveau, self.stations+'_aeronet_'+self.niveau+'_'+self.resoTempo+'.csv')
        except AttributeError as e:
            print e
            try:
                pathcsv = os.path.join(self._ddirDB, 'in_situ', self.mesure, self.stations+'_'+self.mesure+'_'+self.resoTempo+'.csv')
            except AttributeError as e:
                print e
                pathcsv = os.path.join(self._ddirDB, 'in_situ/epidemiologie', self.epidemio, self.pays+'_'+self.epidemio+'_'+self.echelle+'.csv')
        return pathcsv
    
    @property
    def carto(self):
        print self.datefin
        self.year = datetime.strptime(self.datefin,"%Y-%m-%d").strftime("%Y")
        if self.decoupage == "aire":
            if self.shape == "all_fs":
        		pathshape = os.path.join(self._ddirDB, 'carto/fs_par_annee', self.shape, '150409_BF_FS_'+self.year+'.shp')
        		if not os.path.exists(pathshape):
        			pathshape = os.path.join(self._ddirDB, 'carto/fs_par_annee/all_fs/150409_BF_FS_2015.shp')
            else:
        		pathshape = os.path.join(self._ddirDB, 'carto/fs_par_annee', self.shape, '150409_BF_FS_'+self.shape+'_'+self.year+'.shp')
        		if not os.path.exists(pathshape):
        			pathshape = os.path.join(self._ddirDB, 'carto/fs_par_annee', self.shape, '150409_BF_FS_'+self.shape+'_2015.shp')
        else:
            pathshape = os.path.join(self._ddirDB, 'carto', self.decoupage, self.pays+'_'+self.decoupage+'_sante.shp')
        return pathshape