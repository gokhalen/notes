#include <stdio.h>
#include "omp.h"

int main(int argc, char *argv[]){
  #pragma omp parallel
  {
    int tid      = omp_get_thread_num();
    int nthreads = omp_get_num_threads(); 
    printf("Hello world! I'm thread %d out of %d threads\n",tid,nthreads);
  }
  return 0;
}
