class CreateFoos < ActiveRecord::Migration
  def change
    create_table :foos do |t|
      t.string :name
      t.float :score

      t.timestamps
    end
  end
end
