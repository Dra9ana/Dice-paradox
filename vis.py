import numpy as np

def generisi_n_dogadjaja(n,m):

    dogadjaji=np.random.rand(n,m)

    dogadjaji[np.where(np.logical_and(dogadjaji>1/6, dogadjaji<=2/6)) ]=2
    dogadjaji[np.where(np.logical_and(dogadjaji>2/6, dogadjaji<=3/6)) ]=3
    dogadjaji[np.where(np.logical_and(dogadjaji>3/6, dogadjaji<=4/6)) ]=4
    dogadjaji[np.where(np.logical_and(dogadjaji>4/6, dogadjaji<=5/6)) ]=5
    dogadjaji[np.where(np.logical_and(dogadjaji>5/6, dogadjaji<=6/6)) ]=6
    dogadjaji[dogadjaji<=1/6]=1;

    return dogadjaji;

def frekvencije(dogadjaji,n,m):
    broj9=0;
    broj10=0;
    sum=0;
    for i in range(0,n):
        sum=0
        for j in range(0,m):
            sum +=dogadjaji[i][j];

        if(sum==9):
            broj9+=1;
        if(sum==10):
            broj10+=1;

    return(broj9/(n+0.0),broj10/(n+0.0));

def ispisi_dogadjaje(dogadjaji,n,m):
    for i in range(0,n):
        print("Bacanje "+str(i)+" je:")
        if(m==2):
           print("( "+str(dogadjaji[i][0])+", "+str(dogadjaji[i][1])+" )")
        else:
           print("( "+str(dogadjaji[i][0])+", "+str(dogadjaji[i][1])+", "+str(dogadjaji[i][2])+" )")
def ispisi_frekvencije(dogadjaji,n,m):
        print("Frekvencije ovog dogadjaja su:")
        freq=frekvencije(dogadjaji,n,m);
        print("Frekvencija 9 je :"+str(freq[0]));
        print("Frekvencija 10 je :"+str(freq[1]));
        print("######################################################")

def simuliraj(novi,m):
    for n in novi:
        print("Za n = "+str(n))
        dogadjaj=generisi_n_dogadjaja(n,m);
        if(n<=20):
            ispisi_dogadjaje(dogadjaj,n,m);
        ispisi_frekvencije(dogadjaj,n,m);


ocekivana_verovatnoca_zbira10=1/36
ocekivana_verovatnoca_ybira9=2/36

novi=[20,36,50,72,100,500,1000,10000,100000]

#simuliraj(novi,2);
simuliraj(novi,3);
