reset

set terminal postscript eps enhanced color"Times-Roman" 18
set autoscale
set lmargin 13
set bmargin 4

set output "deltaT.eps"

set ylabel"{/*1.5{/Italic delta T}" offset 1,0
set xlabel"{/*1.5{/Italic t(s)} }" offset 0,0

#set xrange[0:51.5]
#set yrange[0:0.0015]

plot "deltaT.dat"  using ($1):($3) notitle"{Max}" with lines lt 1 lw 2.5


