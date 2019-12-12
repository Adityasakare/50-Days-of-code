main ()
{
	int i,a,b,c,choise;
	
	printf("1.Addition\n");
	printf("2.even or odd\n");
	printf("3.Natural no.\n");
	scanf("%d", &choise);
	
	switch(choise)
	{
	
                    case 1:
                    	    printf("Enter the number");
                    	    scanf(" %d %d",&a, &b);
c=a+b;
                    	    printf("The sum is %d",c);
                    	    break;
                    	    
                    	



	case 2:
		   printf("Enter the Number");
		   scanf("%d", &a);
		   if(a%2==0)
		   printf("Even");
		   else
		   printf("odd");
		   break;
	
		
case 3:
	
	   printf("Enter the number");
	   scanf("%d",&a);
	   for(i=0;i<=a;i++)
	   printf("\n%d",i);
	   
}
	   



}
getch();
