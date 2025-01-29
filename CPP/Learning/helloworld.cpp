#include <iostream>
#include <cmath>

//namespace
namespace first{
    int x = 1;
}

namespace second{
    int x = 2;
}

//typedef or using
typedef std::string text_t; //"nicknames" to datatypes, for ease of use
using text_u = std::string; //using is better practice

int main(){
    //comment: no comment
    /*
    Multiline comment
    */

    //Basics, data types
    int age = 25;
    char ng = 'g';
    int x = 3;
    std::string name = "Bro";
    std::cout << "Hello" << std::endl;
    std::cout << "Hi, " << name << "\n";
    std::cout << "You are " << age << " years old\n";

    //logical operators
    //&& and, || or, ! not

    //input
    // std::cin >> name;
    // std::getline(std::cin, name);

    //Constant
    const double PI = 3.14159; //PI is now read-only
    const int LIGHTSPEED = 299792458;

    //Use of namespaces
    /*
    can also use: 
    using namespace first; 

    Instead of 
    std::string name = "Bro";
    use
    using std::string;
    string name = "Bro";
    */ 
    std::cout << x << std::endl;
    std::cout << first::x << std::endl;
    std::cout << second::x << std::endl;
    
    //typedef
    text_t fruit = "banana";
    text_u berry = "blueberry";

    //math, uses cmath
    double z;
    //z = std::max(5,10) // outputs 10
    //z = std::min(5,10) // outputs 5
    //z = pow(2,4);
    //z = sqrt(25);
    //z = abs(-3);
    //z = round(9.9)
    //z = ceil(9.3)
    //z = floort(9.5)

    //if-else
    if(age >= 18){
        std::cout << "is adult" <<std::endl;
    }
    else if(age > 0){
        std::cout << "unborn" <<std::endl;
    }
    else{
        std::cout << "is not adult" <<std::endl;
    }

    //switch
    int month = 13;
    switch(month){
        case 1:
            std::cout << "January" <<std::endl;
            break;
        case 2:
            std::cout << "February" <<std::endl;
            break;
        case 7:
            std::cout << "July" <<std::endl;
            break;
        default:
            std::cout << "please, month a number 1-12" <<std::endl;
    }

    //ternary operator ? - works as if/else
    int n = 9;
    n > 10 ? std::cout << "above 10" << std::endl : std::cout << "10 or less" << std::endl;

    return 0;
}