public class GameOfLife
{
    public static void main(String[] args)
    {
        int x = 10, y = 10;
        int[][] grid = { { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 1, 1, 1, 0, 0, 0, 0, 0, 0 },
                { 0, 0,1, 1, 1, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 } };

        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                if (grid[i][j] == 0)
                    System.out.print(0);
                else
                    System.out.print(1);
            }
            System.out.println();
        }
        System.out.println();
        newGeneration(grid, x, y);
    }

    static void newGeneration(int grid[][], int x, int y)
    {
        int[][] future = new int[x][y];
        for (int l = 1; l < x - 1; l++)
        {
            for (int m = 1; m < y - 1; m++)
            {
             int aliveNeighbours = 0;
                for (int i = -1; i <= 1; i++)
                    for (int j = -1; j <= 1; j++)
                        aliveNeighbours += grid[l + i][m + j];

                aliveNeighbours -= grid[l][m];

                // rule-1(less than 2 live neighbours)
                if ((grid[l][m] == 1) && (aliveNeighbours < 2))
                    future[l][m] = 0;
                // rule-2(more than 3 live neighbours)
                else if ((grid[l][m] == 1) && (aliveNeighbours > 3))
                    future[l][m] = 0;
                // rule-4(exact 3 live neighbours come to life)
                else if ((grid[l][m] == 0) && (aliveNeighbours == 3))
                    future[l][m] = 1;
                // Remains the same
                else
                    future[l][m] = grid[l][m];
            }
        }

        System.out.println("Next Generation");
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                if (future[i][j] == 0)
                    System.out.print(0);
                else
                    System.out.print(1);
            }
            System.out.println();
        }
    }
}
