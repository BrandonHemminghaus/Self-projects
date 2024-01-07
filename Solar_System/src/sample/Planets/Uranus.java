package sample.Planets;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;

public class Uranus {
    public Uranus(Button btn_uranus, Stage primaryStage) {
        btn_uranus.setOnAction(new EventHandler<ActionEvent>() {
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
