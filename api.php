<?php

// Путь к CSV файлу с пользователями
$csvFile = 'users.csv';

// Функция для добавления нового пользователя
function addUser($id)
{
    $apiKey = generateApiKey(); // Генерация API ключа
    $data = [$id, $apiKey];
    $fp = fopen('users.csv', 'a');
    fputcsv($fp, $data);
    fclose($fp);
    return ['id' => $id, 'apiKey' => $apiKey];
}

// Функция для генерации API ключа
function generateApiKey()
{
    return substr(str_shuffle('0123456789'), 0, 16);
}

// Функция для проверки существования пользователя по API ключу
function validateUser($apiKey)
{
    $file = fopen('users.csv', 'r');
    while (!feof($file)) {
        $userData = fgetcsv($file);
        if ($userData !== false && isset($userData[1]) && $userData[1] === $apiKey) {
            fclose($file);
            return true;
        }
    }
    fclose($file);
    return false;
}

// Проверка наличия ключа и запуск соответствующей функции
if (isset($_GET['key'])) {
    $apiKey = $_GET['key'];

    if (isset($_GET['adduser']) && isset($_GET['adduser'])) {
        $id = $_GET['adduser'];
        $response = addUser($id);
        echo json_encode($response);
    } elseif (isset($_GET['validateuser'])) {
        $apiKeyToValidate = $_GET['validateuser'];
        $isValid = validateUser($apiKeyToValidate);
        echo json_encode($isValid);
    } else {
        echo "Invalid request";
    }
} else {
    echo "API key is missing";
}
?>
