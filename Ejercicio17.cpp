#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

double Tmax = 0.5;
double dT = 0.01;
double Xmax = 2;
double dX = 0.01;
int Nt = Tmax/dT;
int Nx = Xmax/dX;

int U(int Nt,int Nx,string nombre);

int main(){
    
    U(Nt,Nx,"Ejercicio17.dat");
    
    return 0;
}

int U(int Nt,int Nx,string nombre){
    
    double x;
    
    double U[Nt+1][Nx+1];

    for(int j=0;j<=Nx;j++){
        x = j*dX;
        U[0][j] = exp(-pow(x-1,2)/(pow(0.25,2)*2));
    }
    
    for(int i=1;i<=Nt;i++){
        U[i][0] = U[0][0];
    }
    
    for(int i=0;i<Nt;i++){
        for(int j=1; j<=Nx; j++){
            U[i+1][j] = U[i][j]-(U[i][j]*dT*(U[i][j]-U[i][j-1])/dX);
        }
    }
    
    ofstream outfile;
    outfile.open(nombre);
    
    for(int i=0; i<=Nt; i++){
        for(int j=0; j<=Nx; j++){
            outfile<<U[i][j]<<"\t";
        }
        outfile<<endl;
    }
    outfile.close();
    
    return 0;
}