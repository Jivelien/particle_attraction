FILENAME=$1

python -m cProfile -o particles.prof $FILENAME
snakeviz particles.prof