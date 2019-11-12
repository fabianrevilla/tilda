%%
clc
close all
clear all
%%
c=0;
vec=load('resultat.txt');
N=[];
t1=[];
t2=[];
t3=[];
t4=[];
t5=[];


for i=1:length(vec)/6;
    N=[N;vec(1+6*c)];
    t1=[t1;vec(2+6*c)];
    t2=[t2;vec(3+6*c)];
    t3=[t3;vec(4+6*c)];
    t4=[t4;vec(5+6*c)];
    t5=[t5;vec(6+6*c)];
    c=c+1;
end
%%
LinSok1=t1;
Linsok2=t2;
Quicksort=t3;
Binary=t4;
Dictionary=t5;
t=table(N,LinSok1,Linsok2,Quicksort,Binary,Dictionary);
t