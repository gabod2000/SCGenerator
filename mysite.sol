pragma solidity ^0.4.11;
contract owned {
  //This is an official solidity snippet from http://solidity.readthedocs.io/en/develop/contracts.html
    function owned() { owner = msg.sender; }
    address owner;
    // This contract only defines a modifier but does not use
    // it - it will be used in derived contracts.
    // The function body is inserted where the special symbol
    // This means that if the owner calls this function, the
    // function is executed and otherwise, an exception is
    // thrown.
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
}
contract C:\Users\sandr\Desktop\WebStart\mysite is owned {


    event AlarmAll(
		 string _id
    );
    function getTriggers()onlyOwner
    returns(
    ){
		return(    }
    function updateAll(
			 string _id
    ) onlyOwner
    {
      if(

      ){
				AlarmAll( _id);
       }
       else{
       }
    }
}