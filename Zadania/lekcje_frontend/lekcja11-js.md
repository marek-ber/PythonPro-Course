# Lekcja: JS podstawy

## 1. Wstęp

Celem lekcji jest wprowadzenie do podstaw JavaScript używanego w przeglądarce. Nauczysz się tworzyć zmienne, rozpoznawać podstawowe typy danych, używać operatorów oraz wyświetlać wyniki w konsoli. Każdy element będzie pokazany na działającym kodzie. Zrozumienie tych podstaw jest konieczne do dalszej pracy z logiką w JavaScript. Kod będzie wykonywany w przeglądarce lub w środowisku Node.js. Skupiamy się na praktycznym użyciu, nie na teorii. Wszystkie przykłady są minimalne i kompletne.

---

## 2. Zagadnienia

## 2.1 Zmienne: let i const

### Koncepcja:

Zmienne służą do przechowywania danych. `let` pozwala zmieniać wartość, `const` tworzy stałą, której nie można nadpisać.

### Kod:

```javascript
let age = 25;
age = 26;

const name = "Anna";

console.log(age);
console.log(name);
```

### Wyjaśnienie:

* `let age = 25` tworzy zmienną, którą można zmienić
* `age = 26` nadpisuje poprzednią wartość
* `const name = "Anna"` tworzy stałą, której nie można zmienić
* `console.log()` wypisuje wartości do konsoli

---

## 2.2 Typy danych

### Koncepcja:

JavaScript ma różne typy danych, które określają rodzaj przechowywanej wartości. Najczęściej używane to liczby, tekst i wartości logiczne.

### Kod:

```javascript
let number = 10;
let text = "Hello";
let isActive = true;

console.log(number);
console.log(text);
console.log(isActive);
```

### Wyjaśnienie:

* `number` przechowuje liczbę
* `text` przechowuje ciąg znaków (string)
* `isActive` przechowuje wartość logiczną (true/false)
* `console.log()` pozwala sprawdzić wartości w konsoli

---

## 2.3 Operatory

### Koncepcja:

Operatory pozwalają wykonywać działania na danych, np. matematyczne lub porównania.

### Kod:

```javascript
let a = 10;
let b = 5;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);

console.log(a > b);
console.log(a === b);
```

### Wyjaśnienie:

* `+ - * /` wykonują podstawowe działania matematyczne
* `>` sprawdza, czy lewa strona jest większa
* `===` sprawdza, czy wartości są równe
* wynik porównań to `true` lub `false`

---

## 2.4 console.log

### Koncepcja:

`console.log` służy do wyświetlania danych w konsoli, co pozwala sprawdzać działanie kodu.

### Kod:

```javascript
console.log("Start programu");

let value = 42;
console.log(value);

console.log(2 + 2);
```

### Wyjaśnienie:

* pierwszy log wypisuje tekst
* drugi wypisuje wartość zmiennej
* trzeci wypisuje wynik działania
* konsola służy do debugowania

---

## 3. Podsumowanie

* `let` umożliwia zmianę wartości zmiennej
* `const` tworzy stałą
* podstawowe typy: number, string, boolean
* operatory wykonują działania i porównania
* `console.log` wyświetla dane
* JavaScript działa na wartościach i operacjach na nich

---

## 4. Zadanie praktyczne

Utwórz plik JavaScript i:

* zadeklaruj zmienną `city` (tekst)
* zadeklaruj zmienną `temperature` (liczba)
* zadeklaruj stałą `isRaining` (boolean)
* wykonaj operacje: dodawanie i porównanie dwóch liczb
* wypisz wszystko w konsoli przy użyciu `console.log`
