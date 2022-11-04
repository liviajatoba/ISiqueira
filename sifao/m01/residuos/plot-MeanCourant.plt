reset

set terminal postscript eps enhanced color"Times-Roman" 18
set autoscale
set lmargin 13
set bmargin 4

set output "Courant-Mean.eps"

set ylabel"{/*1.5{/Italic Mean Courant}" offset 1,0
set xlabel"{/*1.5{/Italic t(s)} }" offset 0,0

plot "../logs/CourantMean_1"  using ($1):($2) notitle"{Max}" with lines lt 1 lw 2.5


