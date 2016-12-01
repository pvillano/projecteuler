/**
 * Created by Rocky on 12/1/2016.
 */
public class p30 {
    public static void main(String[] args) {
        int h = 0;
        long sum = -1;
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                for (int k = 0; k < 10; k++) {
                    for (int l = 0; l < 10; l++) {
                        for (int m = 0; m < 10; m++) {
                            for (int n = 0; n < 10; n++) {
                                if(i*i*i*i*i + j*j*j*j*j + k*k*k*k*k + l*l*l*l*l + m*m*m*m*m + n*n*n*n*n == h){
                                    sum += h;
                                    System.err.println(sum);
                                }
                                h++;
                            }
                        }
                    }
                }
            }
        }
    }
}
