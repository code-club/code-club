class Vote < ActiveRecord::Base
	belongs_to :left, :class_name => 'Foo', :foreign_key => 'left_id'
	belongs_to :right, :class_name => 'Foo', :foreign_key => 'right_id'


	def winner_foo
		return (if winner then left else right end)
	end
	
	def winner_id
		return winner_foo.id
	end
	
	def winner_name
		return winner_foo.name
	end
end
