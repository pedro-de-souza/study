class AulaThreads {
    public static void main(String[ ] args) {
        Loader obj = new Loader();
        obj.start();
    }
}

class Loader extends Thread {
    public void run() {
        System.out.println("Hello");
    }
}