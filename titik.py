import mapnik
m = mapnik.Map(2000,1000)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
r.symbols.append(polygon_symbolizer)

# line_symbolizer = mapnik.LineSymbolizer()
# line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'),2)
# line_symbolizer.stroke_width = 10.0
# r.symbols.append(line_symbolizer)

# point_sym = mapnik.PointSymbolizer()
# point_sym.allow_overlap = True
# point_sym = mapnik.MarkersSymbolizer()
# point_sym.filename
# r.symbols.append(point_sym)

# basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[Point]'), 'DejaVu Sans Bold',9,mapnik.Color('red'))
# basinsLabels.halo_fill = mapnik.Color('yellow')
# basinsLabels.halo_radius = 2
# r.symbols.append(basinsLabels)

# point_sym = mapnik.PointSymbolizer()
# point_sym.allow_overlap = True
# r.symbols.append(point_sym)
# s.rules.append(r)


s.rules.append(r)
m.append_style('Mellyn',s)
ds = mapnik.Shapefile(file="INDONESIA_PROP.shp")
layer = mapnik.Layer('indonesia')
layer.datasource = ds
layer.styles.append('Mellyn')
m.layers.append(layer)

# s = mapnik.Style()
# r = mapnik.Rule()

# line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
# r.symbols.append(line_symbolizer)
# s.rules.append(r)

# point_sym = mapnik.PointSymbolizer()
# point_sym.allow_overlap = True
# point_sym = mapnik.MarkersSymbolizer()
# r.symbols.append(point_sym)
# s.rules.append(r)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[qgis]'), 'DejaVu Sans Bold',3,mapnik.Color('yellow'))
basinsLabels.halo_fill = mapnik.Color('Purple')
basinsLabels.halo_radius = 1
r.symbols.append(basinsLabels)

# point_sym = mapnik.PointSymbolizer()
# point_sym.allow_overlap = True
# point_sym = mapnik.MarkersSymbolizer()
# r.symbols.append(point_sym)
# s.rules.append(r)


s.rules.append(r)
m.append_style('Mellyn2',s)
ds = mapnik.Shapefile(file="titik.shp")
layer = mapnik.Layer('indonesia2')
layer.datasource = ds
layer.styles.append('Mellyn2')
m.layers.append(layer)


m.zoom_all()
mapnik.render_to_file(m,'indonesia.pdf','pdf')
print "rendered image to 'indonesia.pdf' "