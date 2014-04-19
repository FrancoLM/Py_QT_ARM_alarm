/*
===============================================================================
 Name        : main.c
 Author      : $(author)
 Version     :
 Copyright   : $(copyright)
 Description : main definition
===============================================================================
*/

#ifdef __USE_CMSIS
#include "LPC17xx.h"
#endif

//ADC
#include "freq.h"
#include "adc.h"
#include "debug.h"
#include "small_systick.h"

//UART
#include "type.h"
#include "uart.h"
#include <string.h>


#include <cr_section_macros.h>


volatile uint32_t SysTickCount;		/* counts 10ms timeTicks */
uint8_t cont;
volatile uint16_t adcCount;

// InitSysTick() sets systick timer to 10 mS
#define InitSysTick(MHz) SysTick_Config(MHz * (1000000/100))

/*----------------------------------------------------------------------------
  SysTick_Handler
 *----------------------------------------------------------------------------*/
void SysTick_Handler(void) //interrumpe cada 10 milisegundos
{
	char mensaje[8];
	SysTickCount++; /* provee delay */

	if (SysTickCount < 100) return; //100 = 1 segundo

	//Tomamos el valor leido por el sensor
	adcCount = ADC0Read(0);  //Se lee el puerto P0[23]

	//Convierte el valor medido a caracteres (un caracter por cada
	//digito decimal)
	itoa(adcCount, mensaje, 10);

	//Agrega un retorno de carro y nueva línea al mensaje
	strcat(mensaje, "\r\n");

	//Enviamos por UART el valor:
	UARTSend(3, (uint8_t *)mensaje , strlen(mensaje) );

	SysTickCount = 0;

	//Prende y apaga un LED para saber que el sistema está funcionando:
	//Sirve como control
	if (cont == 0){
		LPC_GPIO0->FIOCLR = (1 << 22); // P0[22] = 0
		cont = 1;
	}
	else {
		LPC_GPIO0->FIOSET = (1 << 22); // P0[22] = 1
		cont = 0;
	}
}



int main(void) {

    // TODO: insert code here
	adcCount = 1000;

	LPC_GPIO0->FIODIR |= (1 << 22); // P0[22] COMO SALIDA.


	ADCInit(ADC_CLK);  //Inicializa el ADC. Entrada ADC por el puerto P0[23].
	cont = 0;
	InitSysTick(100);  //Inicializa el Timer para que interrumpa cada 10 ms.

	//UART Setting
	UARTInit(3, 9600);	/* baud rate setting */


    // Force the counter to be placed into memory
    volatile static int i = 0 ;
    // Enter an infinite loop, just incrementing a counter
    while(1) {
        i++ ;
    }
    return 0 ;
}
