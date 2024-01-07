package sample.Planets;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;

public class Jupiter {
    public Jupiter(Button btn_jupiter, Stage primaryStage) {
        btn_jupiter.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                Group root = new Group();
                Scene scene = new Scene(root,500,500);
                primaryStage.setScene(scene);
                primaryStage.show();
            }
        });
    }
}
