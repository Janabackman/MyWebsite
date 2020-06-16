#include <iostream>
#include <string>
using namespace std;

int main(){
	
	string pname[5];
	int pscore[5];
	string name;
	int score;
	int sumScores = 0;
	//input name an score of each player and add it to arrays
	for (int i=0; i<5; ++i){
		cout<< "Enter name of player: ";
		getline(cin, name);
		pname[i]=name;
		cout<< "Enter points score by "<<name<<": ";
		cin>>score;
		cin.ignore();
		pscore[i]=score; 
		sumScores+= score;
		
	}// end for
	
	int average= sumScores/ 5;// divide sum of score by the lengh of the array (5) to get average 
	cout<<"\nThe sum of points score by all players: "<< sumScores<<"\n";
	cout<<"The average of points score by players: "<<average<<"\n";
	
	//get the max score
	int maxScore = pscore[0];
	for (int n; n<5; n++){
		if (pscore[n]>maxScore){
			maxScore= pscore[n];
		}
	}
	
	//get index of the higer score to get the name
	int j;
	for (j; j<5; j++){
		if (pscore[j]==maxScore){
			break;
		}
	}
	cout<<"\nThe player with the higest score is: "<< pname[j];
	cout<<" With "<<maxScore<<" points.";
	
	return 0;
}
