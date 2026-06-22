# Lekcja: funkcje i struktury danych (JS)

## 1. Wstęp

Celem lekcji jest wprowadzenie do podstawowych narzędzi organizacji danych i logiki w JavaScript. Nauczysz się tworzyć funkcje, przechowywać dane w tablicach i obiektach oraz przechodzić po danych w pętli. Każdy element zostanie pokazany w formie działającego kodu. Te mechanizmy są fundamentem większości aplikacji frontendowych. Bez nich nie da się przetwarzać list ani budować logiki UI. Skupiamy się na prostych, bezpośrednich przykładach. Każdy blok kodu jest niezależny.

---

## 2. Zagadnienia

## 2.1 Funkcje

### Koncepcja:

Funkcja to blok kodu, który można uruchamiać wielokrotnie. Przyjmuje dane wejściowe i może zwracać wynik.

### Kod:

```javascript
function add(a, b) {
  return a + b;
}

let result = add(3, 5);

console.log(result);
```

### Wyjaśnienie:

* `function add(a, b)` definiuje funkcję z dwoma parametrami
* `return` zwraca wynik działania funkcji
* `add(3, 5)` wywołuje funkcję z wartościami
* `result` przechowuje wynik
* `console.log` wyświetla rezultat

---

## 2.2 Tablice

### Koncepcja:

Tablica przechowuje wiele wartości w jednej zmiennej. Umożliwia dostęp po indeksie.

### Kod:

```javascript
let fruits = ["apple", "banana", "orange"];

console.log(fruits);
console.log(fruits[0]);
console.log(fruits[2]);
```

### Wyjaśnienie:

* `[]` tworzy tablicę
* elementy są oddzielone przecinkami
* indeks zaczyna się od 0
* `fruits[0]` to pierwszy element
* `console.log` pokazuje całą tablicę i pojedyncze elementy

---

## 2.3 Obiekty

### Koncepcja:

Obiekt przechowuje dane w parach klucz–wartość. Umożliwia opis rzeczy w strukturze.

### Kod:

```javascript
let user = {
  name: "Anna",
  age: 25,
  isActive: true
};

console.log(user);
console.log(user.name);
console.log(user.age);
```

### Wyjaśnienie:

* `{}` tworzy obiekt
* `name`, `age`, `isActive` to klucze
* wartości są przypisane do kluczy
* dostęp przez `user.name`
* obiekty grupują powiązane dane

---

## 2.4 Iteracja: for i map

### Koncepcja:

Iteracja pozwala przejść przez wszystkie elementy tablicy i wykonać na nich operację.

### Kod:

```javascript
let numbers = [1, 2, 3, 4];

for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}

let doubled = numbers.map(function (num) {
  return num * 2;
});

numbers.forEach(function (num){
  console.log(num)
})

console.log(doubled);
```

### Wyjaśnienie:

* `for` przechodzi po indeksach tablicy
* `numbers.length` określa długość tablicy
* `numbers[i]` pobiera element
* `map` tworzy nową tablicę na podstawie starej
* funkcja w `map` przetwarza każdy element

---

## 3. Podsumowanie

* funkcja wykonuje blok kodu wielokrotnie
* tablica przechowuje wiele wartości
* obiekt przechowuje dane klucz–wartość
* `for` iteruje po indeksach
* `map` tworzy nową tablicę
* struktury danych organizują informacje w programie

---

## 4. Zadanie praktyczne

Utwórz plik JavaScript i:

* stwórz funkcję `multiply(a, b)` zwracającą wynik mnożenia
* utwórz tablicę z 5 liczbami
* stwórz obiekt `product` z polami: name, price, inStock
* użyj `for` do wypisania wszystkich liczb z tablicy
* użyj `map`, aby podwoić wartości tablicy
* wypisz wyniki w konsoli
