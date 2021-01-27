#!/bin/bash
#SBATCH -N 1
#SBATCH -C haswell
#SBATCH -q interactive
#SBATCH -J dani4gisaxs
#SBATCH --mail-user=dushizima@lbl.gov
#SBATCH --mail-type=ALL
#SBATCH -t 00:30:00

#OpenMP settings:
export OMP_NUM_THREADS=64
export OMP_PLACES=threads
export OMP_PROC_BIND=close


#run the application:
conda activate cenoura#module load cenoura
srun -n 1 -c 64 --cpu_bind=cores automl.py
