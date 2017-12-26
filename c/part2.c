#include <stdlib.h>
#include <stdio.h>
#include <time.h>

/**
 * Function: oddball
 * Description: Baseline implementation for finding the number that
 *   occurs only once in the array.
 * Arguments:
 *   arr - pointer to start of integer array
 *   len - number of elements in array
 * Return:
 *   The number that occurs only once
 */
#ifdef DEFAULT
int oddball_old(int *arr, int len) {
	int i, j;
	int foundInner;
	int result = 0;

	for (i = 0; i < len; i++) {
		foundInner = 0;
		for (j = 0; j < len; j++) {
			if (i == j) {
				continue;
			}
			if (arr[i] == arr[j]) {
				foundInner = 1;
			}
		}
		if (foundInner != 1) {
			result = arr[i];
		}
	}

	return result;
}
#endif


int oddball_sort(int *arr, int len) {// running time of o(nlogn)
	sort(arr);// implementation of sort array not  shown here. but there are algorithms who could do it in nlogn running time
	int i, j;
	int foundInner;
	int result = 0;
	// the following for loop runs in o(n)
	for (i = 0; i < len-1; i=i+2) {// the duplicated numbers will be in sequence after sort, so jump in step of 2
		if(arr[i]!=arr[i+1]) return arr[i];// check if the number next to the current number is different. if so, answer found, return it
	}
	return 0;// this should never happen if the answer is guaranteed to exits
	// the totla running time is o(nlogn)
}


// The following function runs in o(n) time. It makes use of the popular math equation that says sum of the first n numbers is
// is given by n(n+1)/2. but if the numbers are duplicated, the sum becomes n(n+1). So we can find the missing number by subtracting from this sum
// the sum of elements in the array 	
int oddball(int *arr, int len) {// len is always odd
	int i;
	int n=(len+1)/2;
	int sum_full=n*(n+1);
	int sum_missing=0;
	for(i = 0; i < len; i++){
		sum_missing+=arr[i];
	}
	return sum_full-sum_missing;
}


/**
 * Function: randGenerator
 * Description: Generate a random array that is in compliance with
 *   lab specification
 * Arguments:
 *   arr - pointer to start of integer array
 *   len - number of elements in array
 * Return:
 *   Unused, but feel free to utilize it.
 */
#ifndef RNG
int randGenerator(int *arr, int len) {
	int i, j, r, rcount;
	for (i = 0; i < len; i++) {
		do {
			rcount = 0;
			r = rand()%(len/2 + 1) + 1;
			for (j = 0; j < i && rcount < 2; j++) {
				if (arr[j] == r) {
					rcount++;
				}
			}
		} while(rcount >= 2);
		arr[i] = r;
		//printf("%d ", r);
	}
	//printf("\nDone generating\n");
	return 0;
}

#else
int randGenerator(int *arr, int len) {
	/* Put your code here */
	return 0;
}
#endif


