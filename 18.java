/**
 * Created by Rocky on 11/20/2016.
 */

import static java.lang.Math.max;

public class p18 {
    public static void main(String[] args) {
        int inf = Integer.MAX_VALUE;
        int[][] list = {{75},
                        {95, 64},
                        {17, 47, 82},
                        {18, 35, 87, 10},
                        {20, 4, 82, 47, 65},
                        {19, 1, 23, 75, 3, 34},
                        {88, 2, 77, 73, 7, 63, 67},
                        {99, 65, 4, 28, 6, 16, 70, 92},
                        {41, 41, 26, 56, 83, 40, 80, 70, 33},
                        {41, 48, 72, 33, 47, 32, 37, 16, 94, 29},
                        {53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14},
                        {70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57},
                        {91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48},
                        {63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31},
                        {4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23}};
        int[] costToHere = new int[list.length];
        int[] next = new int[list.length];
        for (int i = 0; i < list.length; i++) {
            for (int j = 0; j < list[i].length - 1; j++) {
                next[j] = costToHere[j];
            }
            for (int j = 0; j < list[i].length - 1; j++) {
                next[j + 1] = max(next[j + 1], costToHere[j]);
            }
            for (int j = 0; j < list[i].length; j++) {
                next[j] += list[i][j];
            }
            int[] temp = costToHere;
            costToHere = next;
            next = temp;
        }
        int best = Integer.MIN_VALUE;
        for (int i = 1; i < costToHere.length; i++) {
            if(costToHere[i] > best){
                best = costToHere[i];
            }
        }
        System.out.println(best);
    }
}
