package main

import (
	"log/slog"
	"net/http"
	"os"

	"github.com/labstack/echo/v4"
	"github.com/joho/godotenv"
)

func main() {
	e := echo.New()
	err := godotenv.Load(".env")
	if err != nil {
		slog.Info(".env file not found, using default values")
	}

	port := ":1323"
	if val, ok := os.LookupEnv("FUNCTIONS_CUSTOMHANDLER_PORT"); ok {
        port = ":" + val
    }

	e.POST("/api/create", func(c echo.Context) error {
		slog.Info("Create inteface called")
		return c.String(http.StatusOK, "Hello, World!")
	})

	e.GET("api/hello", func(c echo.Context) error {
		slog.Info("Hello inteface called")
		return c.String(http.StatusOK, "Hello, Greet!")
	})

	e.Logger.Fatal(e.Start(port))
}