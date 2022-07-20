#ipython --pylab

import aplpy
import math

gc = aplpy.FITSFigure('CII158G0sm.fits')

#gc.show_grayscale()
#gc.show_colorscale(cmap='jet')
gc.show_colorscale()
gc.add_colorbar(pad=0.3,location='right', axis_label_text="erg s$^{-1}$ sr$^{-1}$ cm$^{-2}$")
#gc.add_colorbar.set_axis_label_font(size=12)
gc.axis_labels.set_ytext('log($G_{o}$) [Habing]')
gc.axis_labels.set_xtext('log($n$) [cm$^{-3}$]')
gc.axis_labels.set_font(size=15)
gc.show_markers(math.log10(8600),math.log10(500),marker='o',alpha=1,edgecolor='deepskyblue',facecolor='deepskyblue',s=90)#3.93,2.7
gc.show_contour('CII158G0sm.fits', colors='deepskyblue',levels=[6.52*10**-4,6.88*10**-4],filled=True,alpha=1)


gc.add_label(1.18,6.3,'CII',color='silver',size=18)


gc.add_label(1.8,6.,'northern cloud',color='deepskyblue',size=15)

gc.show_markers(math.log10(6400),math.log10(2400),marker='o',alpha=1,edgecolor='red',facecolor='red',s=90)
gc.show_contour('CII158G0sm.fits', colors='red',levels=[9.72*10**-4,10.08*10**-4],filled=True,alpha=1)
gc.add_label(1.3,5.7,'ridge',color='red',size=15)

gc.show_markers(math.log10(3100),math.log10(1900),marker='o',alpha=1,edgecolor='yellow',facecolor='yellow',s=90)
gc.show_contour('CII158G0sm.fits', colors='yellow',levels=[9.22*10**-4,9.58*10**-4],filled=True,alpha=1)
gc.add_label(1.28,5.4,'shell',color='yellow',size=15)

gc.show_markers(math.log10(2200),math.log10(970),marker='o',alpha=0.5,edgecolor='limegreen',facecolor='limegreen',s=90)
gc.show_contour('CII158G0sm.fits', colors='limegreen',levels=[1.082*10**-3,1.118*10**-3],filled=True,alpha=1)
gc.add_label(1.3,5.1,'pillar',color='limegreen',size=15)

#gc.show_markers(4.15,3,marker='o',alpha=1,edgecolor='orange',facecolor='orange',s=90)
gc.show_markers(math.log10(27000),math.log10(2900),marker='o',alpha=1,edgecolor='darkorange',facecolor='darkorange',s=90)
gc.show_contour('CII158G0sm.fits', colors='darkorange',levels=[2.82*10**-4,3.18*10**-4],filled=True,alpha=1)
gc.add_label(1.15,4.8,'p1',color='darkorange',size=15)

#gc.show_markers(4.65,3.43,marker='o',alpha=1,edgecolor='purple',facecolor='purple',s=90)
#p3-all
gc.show_markers(math.log10(4300),math.log10(2100),marker='o',alpha=1,edgecolor='snow',facecolor='snow',s=90)
gc.show_contour('CII158G0sm.fits', colors='snow',levels=[3.382*10**-3,3.418*10**-3],filled=True,alpha=1) #p3v2
gc.add_label(1.15,4.5,'p3',color='snow',size=15)
#p3_-15_5
gc.show_markers(math.log10(3600),math.log10(790),marker='o',alpha=1,edgecolor='blueviolet',facecolor='blueviolet',s=90)
gc.show_contour('CII158G0sm.fits', colors='blueviolet',levels=[1.982*10**-3,2.018*10**-3],filled=True,alpha=1) #p3v2
gc.add_label(1.28,4.2,'p3v1',color='blueviolet',size=15)
#p3_5_20
gc.show_markers(math.log10(4500),math.log10(2000),marker='o',alpha=0.6,edgecolor='magenta',facecolor='magenta',s=90)
gc.show_contour('CII158G0sm.fits', colors='magenta',levels=[1.182*10**-3,1.218*10**-3],filled=True,alpha=1) #p3v2
gc.add_label(1.28,3.9,'p3v2',color='magenta',size=15)
#,3.382*10**-3,3.418*10**-3 p3

#gc.show_markers(4.34,4.45,marker='o',alpha=1,edgecolor='pink',facecolor='pink',s=90)
gc.show_markers(math.log10(14000),math.log10(32000),marker='o',alpha=1,edgecolor='pink',facecolor='pink',s=90)
gc.show_contour('CII158G0sm.fits', colors='pink',levels=[4.02*10**-4,4.38*10**-4],filled=True,alpha=1)
gc.add_label(1.15,3.6,'p7',color='pink',size=15)

gc.show_markers(math.log10(8600),math.log10(500),marker='o',alpha=1,edgecolor='deepskyblue',facecolor='deepskyblue',s=90)#3



gc.save('cii-g0-n.png')
