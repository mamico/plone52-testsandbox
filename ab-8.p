set terminal png
set output "benchmark-8.png"
set title "ab -n 1000 -c 8 -g out.data http://127.0.0.1:9002/load/largefile"
set size 1,0.7
set grid y
set xlabel "request"
set ylabel "response time (ms)"
plot "bjoern-8-threads-1.data" using 9 smooth sbezier with lines title "python 3.7 wsgi bjoern (1 thread)", \
     "waitress-8-threads-4.data" using 9 smooth sbezier with lines title "python 3.7 wsgi waitress (4 threads)", \
     "waitress-8-threads-1.data" using 9 smooth sbezier with lines title "python 3.7 wsgi waitress (1 thread)", \
     "zserver-8-threads-1.data" using 9 smooth sbezier with lines title "python 2.7 zserver (1 thread)"
