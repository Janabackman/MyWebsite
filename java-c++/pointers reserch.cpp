#include <iostream>
using namespace std;


int main(){
	
	int myNums[4]= {1,2,3,4};
	int* ptrNums;
	ptrNums = myNums;
	for (int i= 0; i<4;i++){
		cout<<"Adress of index "<<i;
		cout<<" "<<ptrNums<<"\n";
		ptrNums++;
	}
	
   
	string name1 = "Uri";
	char middleInitial = 'S';
	string name2 = "Spak";
	int age1 = 27;
	double height = 150.0;
	
	name2= "Backman";
	
	string* ptrFname = &name1;	
	//char* ptrMiddleInitial = &middleInitial;
	string* ptrLname = &name2;
	int* ptrAge= &age1;
	double* ptrWeight= &height;
	
	 
	
	cout<< "Value"<<"\t"<<"Memory adrss\n";
	cout<< name1 <<"\t" << ptrFname<<"\n";
	cout<< middleInitial <<"\t" <<  static_cast<void *>(&middleInitial)<<"\n";
	cout<< name2 <<"\t" << ptrLname<<"\n";
	cout<< age1 <<"\t" << ptrAge<<"\n";
	cout<< height <<"\t" << ptrWeight<<"\n";
	
	cout<<"\n"<<*ptrAge;
	//cout<<"\n"<<*ptrMiddleInitial;
	return 0;
}
