#include "rclcpp/rclcpp.hpp"

class MyNode: public rclcpp::Node {
    public:
        MyNode(): Node("cpp_test"), counter_(0) {
            RCLCPP_INFO(this->get_logger(), "Hello CPP Node");

            //Calls timerCallback every 1 sec
            timer_ = this->create_wall_timer(std::chrono::seconds(1), 
                                             std::bind(&MyNode::timerCallback, this));
        }

    private:
        //creates a timer 
        void timerCallback(){
            RCLCPP_INFO(this->get_logger(), "Hello %d", counter_);
            counter_ += 1;
        }

        rclcpp::TimerBase::SharedPtr timer_;
        int counter_;
};


int main(int argc, char **argv){

    //Starts comms
    rclcpp::init(argc, argv);
    
    
    auto node  = std::make_shared<MyNode>();

    rclcpp::spin(node);

    //Shutsdown comms
    rclcpp::shutdown();
    return 0;
}