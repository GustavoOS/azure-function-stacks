package main

import (
	"log/slog"
	"net/http"
	"strconv"

	"github.com/labstack/echo/v4"
)

var connection = ConnectDB()

func SayHello(c echo.Context) error {
	slog.Info("Create inteface called")
	return c.String(http.StatusOK, "Hello, World!")
}

type ContentRequest struct {
	Color string `json:"color" xml:"color" form:"color" query:"color"`
	Title string `json:"title" xml:"title" form:"title" query:"title"`
}

func CreateResource(c echo.Context) error {
	request := new(ContentRequest)
	if err := c.Bind(request); err != nil {
		return err
	}

	content := Content{Color: request.Color, Title: request.Title}
	connection.Create(&content)
	return c.JSON(http.StatusCreated, content)
}

func ReadResource(c echo.Context) error {
	id, err := strconv.Atoi(c.QueryParam("id"))
	if err != nil {
		slog.Error("Invalid ID", err)
		return c.String(http.StatusBadRequest, "Invalid ID")
	}
	var content Content
	result := connection.First(&content, id)
	if result.Error != nil {
		return c.String(http.StatusNotFound, "Resource not found")
	}
	return c.JSON(http.StatusOK, content)
}


func UpdateResource(c echo.Context) error {
	request := new(ContentRequest)
	if err := c.Bind(request); err != nil {
		return err
	}
	id, err := strconv.Atoi(c.QueryParam("id"))
	if err != nil {
		slog.Error("Invalid ID", err)
		return c.String(http.StatusBadRequest, "Invalid ID")
	}
	idString := strconv.Itoa(id)

	slog.Info("Updating resource", "id", idString)
	var content Content
	connection.First(&content, id)
	if content.Id != int64(id) {
		return c.String(http.StatusNotFound, "Resource not found")
	}

	content.Color = request.Color
	content.Title = request.Title
	connection.Save(&content)
	return c.JSON(http.StatusOK, content)
}

func DeleteResource(c echo.Context) error {
	id, err := strconv.Atoi(c.QueryParam("id"))
	if err != nil {
		slog.Error("Invalid ID", err)
		return c.String(http.StatusBadRequest, "Invalid ID")
	}
	connection.Delete(&Content{}, id)
	return c.String(http.StatusOK, "Resource deleted")
}
